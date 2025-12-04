p=50 c=0;while read l;do d=${l:1};[[ $l == L* ]]&&d=-$d;((p=(p+d)%100,c+=!p));done<input.txt;echo $c
