CREATE MIGRATION m1m6p43nq3ssf3kp3eutf5eknykqy3fw6f3wwoyeatvb5sg4oie43a
    ONTO m162wzagdsbaph2gld7mv7rerep2kvn6456h6qbwh6vxqz3ssft4aa
{
  ALTER TYPE default::Process {
      DROP LINK head;
  };
  ALTER TYPE default::Process {
      CREATE MULTI LINK nodes -> default::Node {
          ON TARGET DELETE ALLOW;
      };
  };
  ALTER TYPE default::Process {
      DROP LINK tail;
  };
};
