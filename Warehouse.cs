using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lab_11_PP
{
    class Warehouse
    {
        int productAmount;
        Dictionary<Product, int> products =
            new Dictionary<Product, int>();
       
        public void addProduct(Product product, int productAmount)
        {
            products.Add(product, productAmount);
        }
        public void update(Product product, int productAmount)
        {
            if(products.ContainsKey(product))
            {
                products[product] = productAmount;
            }    


        }
        public int amountOfProducts()
        {
            int value =0;
            foreach (KeyValuePair<Product, int> dict in products)
            {
                value += dict.Value;
            }
            Console.WriteLine("All amount of products: " + value);
            return value;
        }
        public void allProducts()
        {
           foreach(KeyValuePair<Product, int> dict in products)
            {
                Console.WriteLine("{0}, Value: {1}", dict.Key, dict.Value);
            }
        }

    }
}
