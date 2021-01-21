using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Numerics;
using System.Diagnostics;
using System.IO;
using System.Collections;

namespace lab_11_PP
{
    class Program
    {
        static void Main(string[] args)
        {
            // 1 + 2
            Category category = new Category(1, "meble", "wielka, drewniana");
            Supplier supplier = new Supplier(1, "Philips", "Pila", "signify.com");
            Product product = new Product(1, "szafka", category, supplier, 1000);
            Product product1 = new Product(2, "lozko", category, supplier, 200);
            Warehouse warehouse = new Warehouse();

            warehouse.addProduct(product, 10);
            warehouse.addProduct(product1, 2);
            warehouse.update(product, 5);
            warehouse.allProducts();
            warehouse.amountOfProducts();
            //Console.WriteLine(category.ToString());
            //Console.WriteLine(supplier.ToString());
            //Console.WriteLine(product.ToString());

            // 3
            int n = 5;
            BigInteger silnia = new BigInteger(1);
            System.Diagnostics.Stopwatch stopWatch = new Stopwatch();
            stopWatch.Start();
            if (n == 0)
            {
                Console.WriteLine(silnia);
            }
            else
            {
                for (int i = 1; i < n; i++)
                {
                    silnia = BigInteger.Multiply(silnia, i);
                    Console.WriteLine(silnia);
                }
            }
            stopWatch.Stop();
            TimeSpan ts = stopWatch.Elapsed;
            string elapsedTime = String.Format("{0:00}:{1:00}:{2:00}.{3:00}",
                ts.Hours, ts.Minutes, ts.Seconds, ts.Milliseconds / 10);
            Console.WriteLine("RunTime " + elapsedTime);
            // n=5000 -> 00:01:49.56 czas


            // 4
            
            var dict = new Dictionary<string, int>();
            try
            {
                using (var sr = new StreamReader("Holmes.txt"))
                {
                    char[] delimiterChars = { ' ', ',', '.', ':','"','-', '\t', '\n' };
                    String words = sr.ReadToEnd();
                    string[] wordsList = words.Split(delimiterChars);
                    foreach(var word in wordsList)
                    {
                        word.ToLower();
                        if(word.Length>2)
                        {
                            var count = 0;
                            if(dict.TryGetValue(word, out count))
                            {
                                dict[word]++;
                            }
                            else
                            {
                                dict.Add(word, 1);
                            }
                        }
                    }
                }
            }
            catch(InvalidOperationException e)
            {
                Console.WriteLine("The file could not be read:");
                Console.WriteLine(e.Message);
            }
            int timesToPrint = 0;
            foreach (KeyValuePair<string, int> dic in dict.OrderByDescending(key=> key.Value))
            {
                
                Console.WriteLine("Word: {0}, count: {1}", dic.Key, dic.Value);
                timesToPrint++;
                if(timesToPrint==20)
                {
                    break;
                }

            }
            Console.WriteLine("Press any key to exit.");
            Console.ReadKey();
        }
        
        
    }
}
