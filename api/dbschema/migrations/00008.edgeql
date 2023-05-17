CREATE MIGRATION m1rao2zdp27m2wj34aibyihi36seqtvvo4vusp2h3hunsmwhf6cohq
    ONTO m1f5wk6gdyyzynbkshmf3lhqdbypgmcd7wxxclmvxinagk5lxz6qnq
{
  ALTER TYPE default::Node {
      CREATE PROPERTY receipt -> std::datetime;
  };
};
