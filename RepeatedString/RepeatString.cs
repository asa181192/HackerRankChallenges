using System;

namespace ConsoleApp
{
    class RepeatString
    {

        static void Main(string[] args)
        {
            var number = repeatedString("aba", 10);
            Console.WriteLine(number);
            Console.ReadKey();
        }

        public static long repeatedString(string s, long n)
        {
            long number = 0;
            var pakets = Math.Abs(n / s.Length);
            for (int i = 0; i < s.Length; i++)
            {
                if (s[i] == 'a')
                {
                    number += 1;
                }
            }
            number = pakets * number;
            for (int i = 0; i < (n - (pakets * s.Length)); i++)
            {
                if(s[i] == 'a')
                {
                    number += 1;
                }
            }

            return number;
        }
    }
}
