chan fila = [4] of {int}


active proctype produtor_if(){
	int msg = 1
	
	
	repetir:
	fila!msg
	printf("enviou $d\n",msg)
	msg++
	
	if
	:: msg < 11 -> goto repetir
	:: else -> skip //skip passa e n faz nada
	fi
	
	
}



active proctype produtor_do(){
	int msg = 1

	do
	::msg < 11 ->
		fila!msg
		msg++
	::else-> break
	od
	
}

active proctype consumidor(){
	int msg

	do
	:: fila?msg ->
		printf("recebeu %d\n, msg)
	od


}



