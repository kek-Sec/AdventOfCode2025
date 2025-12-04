BEGIN{p=50}{d=substr($0,2);p=(p+(($0~/^L/?-1:1)*d))%100;c+=p==0}END{print c}
