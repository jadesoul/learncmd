#!/usr/bin/env python
#encoding: utf8

import cmd
import subprocess

class ShellEnabledCmd(cmd.Cmd):
	last_output = ''
	
	def do_shell(this, line):
		'''Run a linux shell command'''
		sub_cmd = subprocess.Popen(line, shell=True, stdout=subprocess.PIPE)
		output = sub_cmd.communicate()[0]
		print output
		this.last_output = output
		
	def do_echo(this, line):
		"""
		Print the input, replacing '$out' with
		the output of the last shell command.
		"""
		# Obviously not robust
		print line.replace('$out', this.last_output)
		
	def do_EOF(this, line):
		return True
		
class HadoopFileSystemCmd(ShellEnabledCmd):
	'''Hadoop File System Cmdine tool'''
	
	prompt='HadoopFileSystemCmd:'
	current_hdir='/home/'
	
	def emptyline(this):
		print 'emptyline()'
		return cmd.Cmd.emptyline(this)
		
	def precmd(this, line):
		print 'precmd(%s)' % line
		return cmd.Cmd.precmd(this, line)
	
	def onecmd(this, s):
		print 'onecmd(%s)' % s
		return cmd.Cmd.onecmd(this, s)
	
	def postcmd(this, stop, line):
		print 'postcmd(%s, %s)' % (stop, line)
		return cmd.Cmd.postcmd(this, stop, line)
	
	def do_ls(this, hdir):
		'''list directory'''
		this.onecmd('hdfs -ls "%s"' % hdir)
		
	def do_l(this, hdir):
		'''list directory'''
		return this.do_ls(hdir)
		
	def do_ll(this, hdir):
		'''list directory'''
		return this.do_ls(hdir)
		
	def do_cd(this, hdir):
		'''change dir into another directory'''
		this.current_hdir+=hdir
		
if __name__ == '__main__':
	HadoopFileSystemCmd().cmdloop()