public class StringCases {
    public static void main(String[] args) {
        String s="Hello World";
        System.out.println(s.indexOf('l'));
        System.out.println(s.lastIndexOf('l'));
        System.out.println(s.indexOf('l',6));
        System.out.println(s.lastIndexOf('l',4));
        String result1=s.repeat(3);
        System.out.println(result1);
        System.out.println(s.startsWith("hel"));
        System.out.println(s.endsWith("rld"));
        String temp="     hello   ";
        String strippedString=temp.strip();
        System.out.println(strippedString);
    }
    
}
