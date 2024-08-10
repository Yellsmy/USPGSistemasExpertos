namespace RedSemanticaEjemploClase
{
    public class Program
    {
        static void Main(string[] args)
        {
            RedSemantica red = new RedSemantica();

            Nodo perro = red.CrearNodo("Perro");
            Nodo animal = red.CrearNodo("Animal");
            Nodo tiene = red.CrearNodo("Tiene");
            Nodo cuatroPatas = red.CrearNodo("Cuatro Patas");

            perro.AgregarArco(animal, "es un");
            perro.AgregarArco(cuatroPatas, "tiene");

            red.MostrarRed();

        }
    }

    public class Nodo
    {
        public string Etiqueta { get; set; }
        public List<Arco> Arcos { get; set; }

        public Nodo(string etiqueta)
        {
            Etiqueta = etiqueta;
            Arcos = new List<Arco>();
        }

        public void AgregarArco(Nodo destino, string etiquetaArco)
        {
            Arcos.Add(new Arco(this, destino, etiquetaArco));
        }
    }


    public class Arco
    {
        public Nodo Origen { get; set; }
        public Nodo Destino { get; set; }
        public string Etiqueta { get; set; }

        public Arco(Nodo origen, Nodo destino, string etiqueta)
        {
            Origen = origen;
            Destino = destino;
            Etiqueta = etiqueta;
        }

        public override string ToString()
        {
            return $"{Origen.Etiqueta} -- {Etiqueta} --> {Destino.Etiqueta}";
        }
    }


    public class RedSemantica
    {
        public List<Nodo> Nodos { get; set; }

        public RedSemantica()
        {
            Nodos = new List<Nodo>();
        }

        public Nodo CrearNodo(string etiqueta)
        {
            var nodo = new Nodo(etiqueta);
            Nodos.Add(nodo);
            return nodo;
        }

        public void MostrarRed()
        {
            foreach (Nodo nodo in Nodos)
            {
                foreach(var arco in nodo.Arcos)
                {
                    Console.WriteLine(arco);
                }
            }
        }
    }
}