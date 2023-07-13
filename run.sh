journalctl -u ssh --no-pager > journal_ssh.log
python3 malicious_ip_finder.py
rm journal_ssh.log
