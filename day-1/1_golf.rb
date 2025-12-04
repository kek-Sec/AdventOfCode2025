p=50;c=0;File.read("input.txt").scan(/(\w)(\d+)/){p=(p+$2.to_i*($1<?R?-1:1))%100;c+=p<1?1:0};p c
