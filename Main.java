public class Main {
    public static void main(String[] args) {
        String s1 = "ABCDEFG";
        String s2 = "PQRST";
        String result = con(subs(s1, 2, len(s2)), subs(s1, len(s2), 2));
        System.out.println(result);
        System.out.println("");
    }

    // 连接两个字符串
    public static String con(String x, String y) {
        return x + y;
    }

    // 返回字符串s从序号i的字符开始的j个字符组成的子串
    public static String subs(String s, int i, int j) {
        return s.substring(i - 1, i - 1 + j);
    }

    // 返回字符串s的长度
    public static int len(String s) {
        return s.length();
    }
}