CREATE MIGRATION m1hxjqdzhllcdhicn5kzbakuzekme64tsofwqvb5fb5bs3jev23ilq
    ONTO m12hifsqmskjmhu32gwnww3hrusbj3wvyfu5p6fc3oodrvb2rchgmq
{
  ALTER TYPE default::Process {
      CREATE LINK realiserGroup -> default::Department {
          ON TARGET DELETE ALLOW;
      };
  };
};
