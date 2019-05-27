import java.util.Scanner;
public class Staircase{
public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
       in.close();
       int k=n;
 while(k!=0){
        for(int i=1;i<=n+1;i++){
             if(i>k){
                 System.out.print("#");
             }
             else{
                 System.out.print(" ");
             }
        }
       System.out.println();
         k--;
    }
        
    }
}


/*

      for(int i=0 ; i<n ;i++){
            for(int j = 0; j <= n-i-2; j++){
                System.out.print(" ");
            }
            for(int j = n-i-1 ; j< n; j++){
                System.out.print("#");
            }
            System.out.println();
        }

*/