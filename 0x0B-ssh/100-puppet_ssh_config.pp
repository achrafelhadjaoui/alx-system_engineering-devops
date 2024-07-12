#!/usr/bin/env bash
# usign puppet to configure a file

file { '/etc/ssh/ssh_config':
	ensure => present,
	content => "
		hosts*
		IdentifyFile ~/.ssh/school
		PasswordAuthentication no
	"
}
