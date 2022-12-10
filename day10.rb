x=[1]
$<.map{|y|a,b=y.split;x+=[x[-1]];x+=[x[-1]+b.to_i]if a<?b}
(0..239).map{|i|(i%40-x[i])**2<2 ? ?# : ?.}.each_slice(40){|y|p y.join}