using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lab_11_PP
{
    class Category
    {
        public int id;
        public string name;
        public string description;
        public Category(int i, string n, string d)
        {
            this.id = i;
            this.name = n;
            this.description = d;
        }

        public override string ToString()
        {
            return "Category: " + id + ", " + name + ", " + description;
        }
    }
}
