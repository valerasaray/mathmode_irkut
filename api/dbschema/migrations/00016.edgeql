CREATE MIGRATION m1ctvtssjhhil72q6ob5ojmfbflxqabc6t4kpi2kpui6hzkrxb3fca
    ONTO m1dvdukj5xks7jdwtxqmj5d6didbv4alaapm2arvyco4xrzqdvmfeq
{
  ALTER TYPE default::Process {
      CREATE LINK head -> default::Node {
          ON TARGET DELETE ALLOW;
      };
      CREATE LINK tail -> default::Node {
          ON TARGET DELETE ALLOW;
      };
  };
};
