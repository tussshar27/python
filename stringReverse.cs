using System;
namespace stringReverse
{
 class stringReverse
 {
 static void Main(string[] args)
 {
 string str = "", reverse = "";
 int Length = 0;
 Console.WriteLine("Enter a Word");
 str = Console.ReadLine();
 Length = str.Length - 1;
 while (Length >= 0)
 {
 reverse = reverse + str[Length];
 Length--;
 }
 Console.WriteLine("Reverse word:");
 Console.WriteLine(reverse);
 Console.ReadLine();
 }
 }
}