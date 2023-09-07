import java.util.*;
public class VarabileSizesArrays2 {
    public static void main(String[] args) {
        //Variable-Sized Arrays
        int[][] arr=new int[3][];
        arr[0]=new int[]{10,20,30,40,50};
        arr[1]=new int[]{1,2,3,4};
        arr[2]=new int[]{3,4};
        for(int i=0;i<3;i++)
        {
            System.out.println(Arrays.toString(arr[i]));
        } 
        
    }
    
}
