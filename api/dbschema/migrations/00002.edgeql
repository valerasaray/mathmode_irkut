CREATE MIGRATION m1cdzbzoxgiztvdcdgktaqqd2kfkbhan5bbcn32c5tmudgkmnqxyxq
    ONTO m16smqiffrfejvy3augh3t5gv6entzyigx3h46sbvcsmsajdtgc6cq
{
  CREATE ABSTRACT TYPE default::Auditable {
      CREATE ANNOTATION std::description := "Add 'create at property to all types.";
      CREATE REQUIRED PROPERTY created_at -> std::datetime {
          SET default := (std::datetime_current());
          SET readonly := true;
      };
  };
  CREATE TYPE default::Right EXTENDING default::Auditable {
      CREATE ANNOTATION std::description := 'Right.';
      CREATE REQUIRED PROPERTY value -> std::str {
          CREATE CONSTRAINT std::exclusive;
          CREATE CONSTRAINT std::max_len_value(50);
      };
  };
  CREATE TYPE default::User EXTENDING default::Auditable {
      CREATE MULTI LINK rights -> default::Right;
      CREATE ANNOTATION std::description := 'User.';
      CREATE PROPERTY FIO -> std::str {
          CREATE CONSTRAINT std::max_len_value(100);
      };
      CREATE REQUIRED PROPERTY login -> std::str {
          CREATE CONSTRAINT std::exclusive;
          CREATE CONSTRAINT std::max_len_value(50);
      };
      CREATE PROPERTY password -> std::str {
          CREATE CONSTRAINT std::max_len_value(50);
      };
  };
  CREATE TYPE default::Comment EXTENDING default::Auditable {
      CREATE ANNOTATION std::description := 'Comment.';
      CREATE MULTI LINK answer -> default::Comment;
      CREATE LINK author -> default::User;
      CREATE REQUIRED PROPERTY text_str -> std::str;
      CREATE REQUIRED PROPERTY updated_at -> std::datetime {
          SET default := (std::datetime_current());
          SET readonly := true;
      };
  };
  CREATE TYPE default::Department EXTENDING default::Auditable {
      CREATE ANNOTATION std::description := 'Department.';
      CREATE LINK boss -> default::User;
      CREATE MULTI LINK staff -> default::User;
      CREATE REQUIRED PROPERTY title -> std::str {
          CREATE CONSTRAINT std::max_len_value(100);
      };
  };
};
