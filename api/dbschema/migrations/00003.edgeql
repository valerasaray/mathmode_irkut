CREATE MIGRATION m1sxw25acpm2ac2kxxlj4m2wu5em744xbgknffuwbxdc6eavrvjiva
    ONTO m1cdzbzoxgiztvdcdgktaqqd2kfkbhan5bbcn32c5tmudgkmnqxyxq
{
  ALTER TYPE default::Comment {
      ALTER LINK answer {
          ON TARGET DELETE ALLOW;
      };
  };
  ALTER TYPE default::Comment {
      ALTER LINK author {
          ON TARGET DELETE ALLOW;
      };
  };
  ALTER TYPE default::Department {
      ALTER LINK staff {
          ON TARGET DELETE ALLOW;
      };
  };
  ALTER TYPE default::User {
      ALTER LINK rights {
          ON TARGET DELETE ALLOW;
      };
  };
};
