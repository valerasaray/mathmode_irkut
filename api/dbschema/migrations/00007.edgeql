CREATE MIGRATION m1f5wk6gdyyzynbkshmf3lhqdbypgmcd7wxxclmvxinagk5lxz6qnq
    ONTO m1hxjqdzhllcdhicn5kzbakuzekme64tsofwqvb5fb5bs3jev23ilq
{
  ALTER TYPE default::Node {
      ALTER LINK node {
          RENAME TO along;
      };
  };
};
