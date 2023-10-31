#!/usr/bin/env ruby
puts ARGV[0].scan(/^[0-9]{10}$/).join if ARGV[0]
