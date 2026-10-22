using System;

namespace GladiatorBattle
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string typeBattle, typeDifficulty;

            double health_1, attack, aftAttHealth_1, health_2, aftAttHealth_2;
            double armor_1, withArmor, armor_2;

        Input:
            try
            {
                Console.Write("Какой бой хотите устроить? Дружеский или одиночный: ");
                typeBattle = Convert.ToString(Console.ReadLine());

                if (typeBattle == "дружеский")
                {
                    //Ввод характиристик перевого гладиатора
                    health_1 = HealthСalculation();
                    
                    Console.Write("Введите показатель брони: ");
                    armor_1 = Convert.ToDouble(Console.ReadLine());


                    //Ввод характиристик второго гладиатора
                    health_2 = HealthСalculation();

                    Console.Write("Введите показатель брони: ");
                    armor_2 = Convert.ToDouble(Console.ReadLine());


                    #region Расчет атаки, конечного здоровья и брони для первого гладиатора
                    attack = RandomDoubleArmor(new Random(), 0, armor_1 * 0.5);
                    Console.WriteLine("Удар: {0}", attack);

                    withArmor = attack * (armor_1 / 100.0);   //Урон с учётом брони

                    // Получение здоровья после удара
                    aftAttHealth_1 = health_1 - withArmor;
                    aftAttHealth_1 = Math.Round(aftAttHealth_1, 2);
                    Console.WriteLine("Здоровье после удара: {0}", aftAttHealth_1);

                    armor_1 -= attack;
                    Console.WriteLine("Остаток брони: {0}", armor_1);
                    #endregion

                    #region Расчет атаки, конечного здоровья и брони для второго гладиатора
                    attack = RandomDoubleArmor(new Random(), 0, armor_2 * 0.5);
                    Console.WriteLine("Удар: {0}", attack);

                    withArmor = attack * (armor_2 / 100.0);   //Урон с учётом брони

                    // Получение здоровья после удара
                    aftAttHealth_2 = health_2 - withArmor;
                    aftAttHealth_2 = Math.Round(aftAttHealth_2, 2);
                    Console.WriteLine("Здоровье после удара: {0}", aftAttHealth_2);

                    armor_2 -= attack;
                    Console.WriteLine("Остаток брони: {0}", armor_2);
                    #endregion

                    if (aftAttHealth_2 > aftAttHealth_1)
                    {
                        Console.WriteLine("Победил Второй гладиатор");
                    }
                    else if (aftAttHealth_2 < aftAttHealth_1)
                    {
                        Console.WriteLine("Победил Первый гладиатор");
                    }
                    else
                    {
                        Console.WriteLine("Ничья");
                    }

                }
                else if (typeBattle == "одиночный")
                {
                    Console.Write("Выберите сложность - мирный, средний, сложный, невозможный: ");
                    typeDifficulty = Convert.ToString(Console.ReadLine());

                    //Ввод здоровья
                    Console.Write("Введите уровень здоровья: ");
                    health_1 = Convert.ToDouble(Console.ReadLine());
                    health_1 = Math.Round(health_1, 2);     //Округляем здоровье до 2-х знаков

                    //Ввод брони
                    Console.Write("Введите показатель брони: ");
                    armor_1 = Convert.ToDouble(Console.ReadLine());

                    Console.WriteLine();

                    // Получение показателя удара
                    switch (typeDifficulty)
                    {
                        case "мирный":
                            attack = RandomDoubleArmor(new Random(), 0, armor_1 * 0.5);
                            break;
                        case "средний":
                            attack = RandomDoubleArmor(new Random(), 0, (armor_1 + health_1));
                            break;
                        case "сложный":
                            attack = RandomDoubleArmor(new Random(), (armor_1 + health_1) * 0.5, (armor_1 + health_1) * 1.5);
                            break;
                        case "невозможный":
                            attack = RandomDoubleArmor(new Random(), (armor_1 + health_1) * 0.5, (armor_1 + health_1) * 4);
                            break;
                    }
                    attack = RandomDoubleArmor(new Random(), 0, armor_1 * 0.5);
                    Console.WriteLine("Удар: {0}", attack);

                    withArmor = attack * (armor_1 / 100.0);   //Урон с учётом брони

                    // Получение здоровья после удара
                    aftAttHealth_1 = health_1 - withArmor;
                    aftAttHealth_1 = Math.Round(aftAttHealth_1, 2);
                    Console.WriteLine("Здоровье после удара: {0}", aftAttHealth_1);

                    // Получение брони после удара
                    armor_1 -= attack;
                    Console.WriteLine("Остаток брони: {0}", armor_1);
                }
            }
            catch
            {
                goto Input;
            }
        }


        /// <summary>
        /// 
        /// </summary>
        /// <param name="random">Объект типа Random</param>
        /// <param name="min">Минимальное значение</param>
        /// <param name="max">Максимальное значение</param>
        /// <returns>Возвращает случайное число в заданном диапазоне</returns>
        public static double RandomDoubleArmor(Random random, double min, double max)
        {
            // NextDouble() возвращает значение в диапазоне [0.0, 1.0)
            double randomValue = random.NextDouble();

            // Масштабируем и сдвигаем результат в нужный диапазон
            double range = max - min;
            double scaledValue = randomValue * range;
            double result = scaledValue + min;
            result = Math.Round(result, 2);

            return result;
        }

        public static double HealthСalculation()
        {
            double health;

            Console.Write("Введите уровень здоровья: ");
            health = Convert.ToDouble(Console.ReadLine());
            health = Math.Round(health, 2);

            return health;
        }
    }
}