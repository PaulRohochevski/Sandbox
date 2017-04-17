#!/usr/bin/python
# _*_ coding:utf-8 _*_
import pexpect
import sys
import re
from StringIO import StringIO

bash = pexpect.spawn('bash --norc')  # --norc нужна, чтобы не читался bashrc

# Читаем приглашение
try:
    prompt = bash.read_nonblocking(size=128, timeout=10)
except pexpect.TIMEOUT:
    pass

prompt = prompt.strip()
print 'Prompt:', prompt

bash.sendline('ls -1')

# re.escape чтобы символы $ и т.п. в приглашении
# не воспринимались как спец-символы регулярного выражения
bash.expect(re.escape(prompt))

# Читаем вывод ls
ls_out = bash.before

for line in StringIO(ls_out).readlines():
    print 'Read:', line.strip()