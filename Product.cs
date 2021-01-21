using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lab_11_PP
{
    class Product
    {
        public int id;
        public string name;
        public Category category;
        public Supplier supplier;
        public decimal unitPrice;

        public Product(int i, string n, Category c, Supplier s, decimal u)
        {
            this.id = i;
            this.name = n;
            this.category = c;
            this.supplier = s;
            this.unitPrice = u;
        }
        public override string ToString()
        {
            return "Product: " + id + ", "+ name +", "+ category.ToString() +", "+ supplier.ToString() +", "+ unitPrice;
        }
    }
}
