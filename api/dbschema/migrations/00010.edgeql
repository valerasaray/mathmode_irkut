CREATE MIGRATION m162wzagdsbaph2gld7mv7rerep2kvn6456h6qbwh6vxqz3ssft4aa
    ONTO m1ehldql7kconngof37bghgpn4gajajkzd2xsmfn7kiw2nb7lndvta
{
  ALTER TYPE default::Comment {
      DROP LINK answer;
  };
  ALTER TYPE default::Comment {
      CREATE PROPERTY answer -> std::str;
  };
  ALTER TYPE default::Comment {
      DROP PROPERTY updated_at;
  };
  CREATE TYPE default::Notification EXTENDING default::Auditable {
      CREATE ANNOTATION std::description := 'Notification.';
      CREATE LINK comment -> default::Comment {
          ON TARGET DELETE ALLOW;
      };
      CREATE LINK new_assign -> default::Process {
          ON TARGET DELETE ALLOW;
      };
      CREATE LINK passed_node -> default::Node {
          ON TARGET DELETE ALLOW;
      };
      CREATE LINK to_department -> default::Department {
          ON TARGET DELETE ALLOW;
      };
      CREATE LINK user_to -> default::User {
          ON TARGET DELETE ALLOW;
      };
  };
};
