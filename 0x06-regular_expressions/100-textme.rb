#!/usr/bin/env ruby
# script should output: [SENDER],[RECEIVER],[FLAGS]
# The sender phone number or name (including country code if present)
# The receiver phone number or name (including country code if present)
# The flags that were used

from = ARGV[0].scan(/(?<=from:)(.*?)(?=\])/)
to = ARGV[0].scan(/(?<=to:)(.*?)(?=\])/)
flag = ARGV[0].scan(/(?<=flags:)(.*?)(?=\])/)

puts [from, to, flag].join(',')
