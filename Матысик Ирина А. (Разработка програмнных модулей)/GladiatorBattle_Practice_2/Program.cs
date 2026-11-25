using System;

namespace GladiatorBattle
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double health_1, health_2, armor_1, armor_2, aftAttHealth_1, aftAttHealth_2;
            double attack, passable_attack;

            #region Ввод характеристик  

            Console.Write("Введите уровень здоровья для первого гладиатора: ");
            health_1 = Convert.ToDouble(Console.ReadLine());
            health_1 = Math.Round(health_1, 2);
            Console.Write("Введите показатель брони для первого гладиатора: ");
            armor_1 = Convert.ToDouble(Console.ReadLine());

            Console.Write("Введите уровень здоровья для второго гладиатора: ");
            health_2 = Convert.ToDouble(Console.ReadLine());
            health_2 = Math.Round(health_2, 2);
            Console.Write("Введите показатель брони для второго гладиатора: ");
            armor_2 = Convert.ToDouble(Console.ReadLine());

            #endregion

            attack = 30;
            while (true)
            {
                Console.WriteLine("Второй гладиатор наносит ударил");

                passable_attack = attack * armor_1/100;
                armor_1 = armor_1 - attack / 100;
                Console.WriteLine("Он нанес {0} урона", passable_attack);

                if (armor_1 < 0)
                {
                    armor_1 = 0;
                    passable_attack = attack;
                }

                health_1 = health_1 - passable_attack;
                health_1 = Math.Round(health_1, 2);
                Console.WriteLine("У первого гладиатора осталось {0} здоровья и {1} брони", health_1, armor_1);

                if (health_1 <= 0)
                {
                    Console.WriteLine("Первый гладиатор погиб. Победил Второй!");
                    break;
                }

                Console.WriteLine("Первый гладиатор наносит ударил");

                passable_attack = attack * armor_2 / 100;
                armor_2 = armor_2 - attack / 100;
                Console.WriteLine("Он нанес {0} урона", passable_attack);

                if (armor_2 < 0)
                {
                    armor_2 = 0;
                    passable_attack = attack;
                }

                health_2 = health_2 - passable_attack;
                health_2 = Math.Round(health_2, 2);
                Console.WriteLine("У второго гладиатора осталось {0} здоровья и {1} брони", health_2, armor_2);

                if (health_2 <= 0)
                {
                    Console.WriteLine("Второй гладиатор погиб. Победил Первый!");
                    break;
                }
            }
            Console.WriteLine("Игра окончина");
        }
    }
}