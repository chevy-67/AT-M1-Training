class java_code{
    public static void main(String[] arg){
        int[] ar = {1,2,3,5,1,6,7,2};
        for(int i=0;i<ar.length;i++){
            if(ar[i]%2==0) System.out.println(ar[i]+" even");
            else System.out.println(ar[i]+" odd");
        }
    }
}