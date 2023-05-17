CREATE MIGRATION m1l5yh2giraokhpnlfmd3m2uqn5qbonnmysbttd2mj4ngfj6i2bngq
    ONTO m1sxw25acpm2ac2kxxlj4m2wu5em744xbgknffuwbxdc6eavrvjiva
{
  ALTER TYPE default::Department {
      ALTER LINK boss {
          ON TARGET DELETE ALLOW;
      };
  };
};
