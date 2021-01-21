using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lab_11_PP
{
    class Supplier
    {
        public int id;
        public string companyName;
        public string city;
        public string homePage;

        public Supplier(int i, string compName, string c, string h)
        {
            this.id = i;
            this.companyName = compName;
            this.city = c;
            this.homePage = h;

        }

        public override string ToString()
        {
            return "Supplier: " + id + ", " + companyName + ", " + city + ", " + homePage;
        }
    }
}
