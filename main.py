# encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import os

from bs4 import BeautifulSoup as bs
import urllib.request

from github_issue import make_github_issue
from config import NEW_SUB_URL, KEYWORD_LIST, KEYWORD_EX_LIST, USERNAME

def main(args):

    
    # TOKEN = args.token
    
    page = urllib.request.urlopen(NEW_SUB_URL)
    soup = bs(page, 'html.parser')
    content = soup.body.find("div", {'id': 'content'})

    issue_title = content.find("h3").text
    dt_list = content.dl.find_all("dt")
    dd_list = content.dl.find_all("dd")
    arxiv_base = "https://arxiv.org/abs/"

    assert len(dt_list) == len(dd_list)

    keyword_list = KEYWORD_LIST
    keyword_ex_list = KEYWORD_EX_LIST
    #keyword_dict = {key: [] for key in keyword_list}
    keyword_dict = []

    for i in range(len(dt_list)):
        paper = {}
        paper_number = dt_list[i].text.strip().split(" ")[2].split(":")[-1]
        paper['main_page'] = arxiv_base + paper_number
        paper['pdf'] = arxiv_base.replace('abs', 'pdf') + paper_number

        paper['title'] = dd_list[i].find("div", {"class": "list-title mathjax"}).text.replace("Title: ", "").strip()
        paper['authors'] = dd_list[i].find("div", {"class": "list-authors"}).text.replace("Authors:\n", "").replace(
            "\n", "").strip()
        paper['subjects'] = dd_list[i].find("div", {"class": "list-subjects"}).text.replace("Subjects: ", "").strip()
        paper['abstract'] = dd_list[i].find("p", {"class": "mathjax"}).text.replace("\n", " ").strip()

        subjects = paper['subjects']
        if not ("astro-ph.GA" in subjects or "astro-ph.SR" in subjects):
            continue

                        
        inclu=0
        for keyword in keyword_list:
            if keyword.lower() in paper['abstract'].lower():
                inclu=1
        for keyword in keyword_list:
            if keyword.lower() in paper['title'].lower():
                inclu=1
        for keyword_ex in keyword_ex_list:
            if (keyword_ex.lower() in paper['abstract'].lower())==1:
                inclu=0
        for keyword_ex in keyword_ex_list:
            if (keyword_ex.lower() in paper['title'].lower())==1:
                inclu=0
        if inclu==1: 
            keyword_dict.append(paper)

    import datetime
    
    full_report = '# '+issue_title+'\n'
    full_report = full_report + 'Auto update Star Formation & Molecular Cloud papers at about 2:30am UTC (10:30am Beijing time) every weekday.'+'\n'
    full_report = full_report + '\n\n'
    full_report = full_report + '阅读 `Usage.md`了解如何使用此repo实现个性化的Arxiv论文推送' + '\n\n'
    full_report = full_report + 'See `Usage.md` for instructions on how to personalize the repo. ' + '\n'
    full_report = full_report + '\n\n'
    full_report = full_report + 'Keyword list: ' + str(keyword_list) + '\n'
    full_report = full_report + '\n\n'
    full_report = full_report + 'Excluded: ' + str(keyword_ex_list) + '\n'
    full_report = full_report + '\n\n'

    full_report = full_report + '### Today: ' + str(len(keyword_dict)) + 'papers \n'
    
    if len(keyword_dict) == 0:
        full_report = full_report + 'There is no result \n'

    for paper in keyword_dict:
        report = '#### {}\n - **Authors:** {}\n - **Subjects:** {}\n - **Arxiv link:** {}\n - **Pdf link:** {}\n - **Abstract**\n {}' \
                .format(paper['title'], paper['authors'], paper['subjects'], paper['main_page'], paper['pdf'],
                        paper['abstract'])
        full_report = full_report + report + '\n'
        
    full_report = full_report + '\n\n'
    full_report = full_report + 'by Al.Zn (Xin Lyu). ' + '\n'
    full_report = full_report + '\n\n'
    full_report = full_report + datetime.datetime.now().strftime("%Y-%m-%d") + '\n'

    # full_report = full_report + '\n</details>'

    # create an md file using full_report, with the name of date, and upload it to github
    # create a date string
    
    filename = './Arxiv_Daily_Notice/'+datetime.datetime.now().strftime("%Y-%m-%d") + '-Arxiv-Daily-Paper.md'
    filename_readme = './README.md'
    print(filename)
    with open(filename, 'w+') as f:
        f.write(full_report)

    with open(filename_readme, 'w+') as f:
        f.write(full_report)

    make_github_issue(title=issue_title, body=full_report,labels=keyword_list, 
    TOKEN=os.environ['TOKEN'])
    
    import smtplib, ssl
    from email.message import EmailMessage
    
    # def send_email_smtp(subject, html_body, plain_body):
    #     host = os.environ.get("SMTP_HOST")
    #     port = int(os.environ.get("SMTP_PORT", "465"))
    #     user = os.environ.get("SMTP_USERNAME")
    #     pwd  = os.environ.get("SMTP_PASSWORD")
    #     sender = os.environ.get("SMTP_FROM")
    #     to = [x.strip() for x in os.environ.get("EMAIL_TO","").split(",") if x.strip()]
    
    #     if not (host and user and pwd and sender and to):
    #         print("[WARN] SMTP not configured; skip email.")
    #         return
    
    #     msg = EmailMessage()
    #     msg["Subject"] = subject
    #     msg["From"] = sender
    #     msg["To"] = ", ".join(to)
    #     msg.set_content(plain_body)
    #     msg.add_alternative(f"<!doctype html><html><body>{html_body}</body></html>", subtype="html")
    
    #     # 465(SSL) 如 163 邮箱；587(STARTTLS) 如 Gmail
    #     if port == 465:
    #         with smtplib.SMTP_SSL(host, port, context=ssl.create_default_context()) as s:
    #             s.login(user, pwd)
    #             s.send_message(msg)
    #     else:
    #         with smtplib.SMTP(host, port) as s:
    #             s.ehlo()
    #             s.starttls(context=ssl.create_default_context())
    #             s.login(user, pwd)
    #             s.send_message(msg)

    # subject = issue_title  # 比如 "Showing new listings for Monday, 20 October 2025"
    # html_body = full_report.replace("\n","<br>")
    # plain_body = full_report
    # send_email_smtp(subject, html_body, plain_body)

    import os, smtplib, ssl, pathlib, re
    from email.message import EmailMessage
    import markdown  # pip install markdown
    
    def send_email_with_md(md_path: str, subject_hint: str = None):
        if not md_path or not os.path.exists(md_path):
            print("[WARN] markdown not found:", md_path)
            return
    
        text = pathlib.Path(md_path).read_text(encoding="utf-8")
        # Markdown -> HTML
        html_body = markdown.markdown(text, extensions=["extra", "nl2br", "sane_lists", "toc"])
        html_tpl = f"""<!doctype html><html><head><meta charset="utf-8">
        <style>
          body {{ font:14px/1.6 -apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial; color:#111 }}
          a {{ text-decoration:none }}
          code, pre {{ font-family: ui-monospace,SFMono-Regular,Menlo,Consolas,monospace }}
          pre {{ background:#f6f8fa; padding:12px; border-radius:8px; overflow:auto }}
        </style></head><body>{html_body}</body></html>"""
    
        # 主题：优先用 md 首个二/三级标题
        m = re.search(r'^\s*#{2,3}\s*(.+)$', text, flags=re.M)
        subject = subject_hint or (m.group(1).strip() if m else f"arXiv Daily · {os.path.basename(md_path)}")
    
        host = os.environ.get("SMTP_HOST")
        port = int(os.environ.get("SMTP_PORT", "465"))
        user = os.environ.get("SMTP_USERNAME")
        pwd  = os.environ.get("SMTP_PASSWORD")
        sender = os.environ.get("SMTP_FROM")
        to = os.environ.get("EMAIL_TO")
        if not all([host, port, user, pwd, sender, to]):
            print("[WARN] SMTP not configured; skip email."); return
    
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = to
        msg.set_content(text)                 # 纯文本备份
        msg.add_alternative(html_tpl, subtype="html")  # HTML 正文
    
        if port == 465:
            with smtplib.SMTP_SSL(host, port, context=ssl.create_default_context()) as s:
                s.login(user, pwd); s.send_message(msg)
        else:
            with smtplib.SMTP(host, port) as s:
                s.ehlo(); s.starttls(context=ssl.create_default_context()); s.login(user, pwd); s.send_message(msg)
    
        print("[OK] Mail sent to", to)

    import glob
    md_files = sorted(glob.glob("Arxiv_Daily_Notice/*.md"), key=os.path.getmtime, reverse=True)
    md_path = md_files[0] if md_files else "README.md"
    send_email_with_md(md_path, subject_hint=issue_title if 'issue_title' in globals() else None)

    print("end")

if __name__ == '__main__':
    #     处理参数，实际只需要TOKEN
    parser = argparse.ArgumentParser(description='Get the TOKEN for github issue')
    parser.add_argument('-t','--token', help='The github TOKEN', required=True, default='Token Needed!')
    args = vars(parser.parse_args())
    # print(args['token'])
    # print(os.environ['TOKEN'])
    main(args)
