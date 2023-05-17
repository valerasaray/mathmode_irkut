CREATE MIGRATION m1ehldql7kconngof37bghgpn4gajajkzd2xsmfn7kiw2nb7lndvta
    ONTO m1rao2zdp27m2wj34aibyihi36seqtvvo4vusp2h3hunsmwhf6cohq
{
  ALTER TYPE default::SubNode {
      ALTER PROPERTY end_correction {
          RESET readonly;
      };
  };
  ALTER TYPE default::SubNode {
      ALTER PROPERTY end_verification {
          RESET readonly;
      };
  };
  ALTER TYPE default::SubNode {
      CREATE PROPERTY main -> std::bool;
  };
  ALTER TYPE default::SubNode {
      ALTER PROPERTY start_verification {
          RESET readonly;
      };
  };
};
