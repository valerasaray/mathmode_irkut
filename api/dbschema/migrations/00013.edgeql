CREATE MIGRATION m1islthvxb7eexwclxkvem6abormpni6xsxwxaqy72pxntqciv3uxa
    ONTO m166zg5bunts2ubdhnphvywnapxsldkwxo7hffwagged7tnfek2cyq
{
  ALTER TYPE default::Status {
      ALTER PROPERTY color {
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
