#!/usr/bin/env ruby
puts ARGV[0].match(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)[1..3].join(",")

