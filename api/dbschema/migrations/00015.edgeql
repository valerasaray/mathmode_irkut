CREATE MIGRATION m1dvdukj5xks7jdwtxqmj5d6didbv4alaapm2arvyco4xrzqdvmfeq
    ONTO m1i4x5hcbgelddjsmemvmimecl67hcxpr3gmplla2qvb6gufbeyj6a
{
  ALTER TYPE default::Node {
      ALTER PROPERTY title {
          DROP CONSTRAINT std::exclusive;
      };
  };
  ALTER TYPE default::SubNode {
      ALTER PROPERTY title {
          DROP CONSTRAINT std::exclusive;
      };
  };
};
