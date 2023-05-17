CREATE MIGRATION m166zg5bunts2ubdhnphvywnapxsldkwxo7hffwagged7tnfek2cyq
    ONTO m1m6p43nq3ssf3kp3eutf5eknykqy3fw6f3wwoyeatvb5sg4oie43a
{
  ALTER TYPE default::Template {
      ALTER PROPERTY title {
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
