import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import lib.jira as jira
import json
from termcolor import colored

def colored_status(status):
	color = None
	if status.strip() == 'Open': color = 'blue'
	elif status.strip() == 'In Progress': color = 'magenta'
	elif status.strip() == 'Resolved': color = 'green'
	else: color = 'yellow'
	return colored(status, color, attrs=['bold'])

def print_results(query):
	try: issues = jira.Issue.search(query)
	except jira.APIException, e:
		print e.response.status, e.response.reason
		print e.response.read()
	for issue in issues:
		print '%s %s %s' % (colored('%-12s' % issue.key, 'cyan'), colored_status('%-13s' % issue.status), issue.summary)

def main(query):
	print_results("summary ~'%s' or comment ~'%s'" % (query,query))

if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1]:
		main(sys.argv[1])
	else:
		print 'Usage: python %s [search]' % __file__
		sys.exit(0)
