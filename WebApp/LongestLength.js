function LongestLength(s)
{
	 var a=s.split(" ");
	var m=a[0].length;
	while(a[i]!='\0')
	{
		if(a[i].length>m)
			m=a[i].length;
	}
	console.log(m);
}
