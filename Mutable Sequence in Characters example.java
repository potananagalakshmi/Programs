public class mutable {
    public static void main(String[] args) {
        StringBuilder sb=new StringBuilder("Hello world");
        System.out.println(sb);
        sb.setCharAt(6,'U');
        System.out.println(sb);
        
    }
}
