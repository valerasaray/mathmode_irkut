CREATE MIGRATION m12hifsqmskjmhu32gwnww3hrusbj3wvyfu5p6fc3oodrvb2rchgmq
    ONTO m1l5yh2giraokhpnlfmd3m2uqn5qbonnmysbttd2mj4ngfj6i2bngq
{
  ALTER TYPE default::Comment {
      ALTER PROPERTY updated_at {
          RESET OPTIONALITY;
      };
  };
  CREATE TYPE default::TitleField EXTENDING default::Auditable {
      CREATE REQUIRED PROPERTY value -> std::str;
  };
  CREATE TYPE default::Field EXTENDING default::Auditable {
      CREATE ANNOTATION std::description := 'Field.';
      CREATE LINK titleField -> default::TitleField {
          ON TARGET DELETE ALLOW;
      };
      CREATE REQUIRED PROPERTY value -> std::str;
  };
  CREATE TYPE default::Status EXTENDING default::Auditable {
      CREATE ANNOTATION std::description := 'Status.';
      CREATE REQUIRED PROPERTY color -> std::str;
      CREATE REQUIRED PROPERTY title -> std::str;
  };
  CREATE TYPE default::SubNode EXTENDING default::Auditable {
      CREATE ANNOTATION std::description := 'SubNode.';
      CREATE MULTI LINK comments -> default::Comment {
          ON TARGET DELETE ALLOW;
      };
      CREATE LINK fit -> default::User {
          ON TARGET DELETE ALLOW;
      };
      CREATE PROPERTY end_correction -> std::datetime {
          SET default := (std::datetime_current());
          SET readonly := true;
      };
      CREATE PROPERTY end_verification -> std::datetime {
          SET default := (std::datetime_current());
          SET readonly := true;
      };
      CREATE PROPERTY start_verification -> std::datetime {
          SET default := (std::datetime_current());
          SET readonly := true;
      };
      CREATE REQUIRED PROPERTY title -> std::str {
          CREATE CONSTRAINT std::exclusive;
          CREATE CONSTRAINT std::max_len_value(50);
      };
  };
  CREATE TYPE default::Node EXTENDING default::Auditable {
      CREATE MULTI LINK customField -> default::Field {
          ON TARGET DELETE ALLOW;
      };
      CREATE ANNOTATION std::description := 'Node.';
      CREATE MULTI LINK assigned -> default::Department {
          ON TARGET DELETE ALLOW;
      };
      CREATE LINK next -> default::Node {
          ON TARGET DELETE ALLOW;
      };
      CREATE LINK node -> default::Node {
          ON TARGET DELETE ALLOW;
      };
      CREATE LINK status -> default::Status {
          ON TARGET DELETE ALLOW;
      };
      CREATE MULTI LINK subs -> default::SubNode {
          ON TARGET DELETE ALLOW;
      };
      CREATE PROPERTY addenable -> std::bool;
      CREATE REQUIRED PROPERTY title -> std::str {
          CREATE CONSTRAINT std::exclusive;
          CREATE CONSTRAINT std::max_len_value(50);
      };
  };
  CREATE TYPE default::Priority EXTENDING default::Auditable {
      CREATE ANNOTATION std::description := 'Priority.';
      CREATE REQUIRED PROPERTY value -> std::str {
          CREATE CONSTRAINT std::exclusive;
          CREATE CONSTRAINT std::max_len_value(50);
      };
  };
  CREATE TYPE default::ProcessType EXTENDING default::Auditable {
      CREATE ANNOTATION std::description := 'ProcessType.';
      CREATE REQUIRED PROPERTY title -> std::str {
          CREATE CONSTRAINT std::exclusive;
          CREATE CONSTRAINT std::max_len_value(50);
      };
  };
  CREATE TYPE default::Process EXTENDING default::Auditable {
      CREATE LINK head -> default::Node {
          ON TARGET DELETE ALLOW;
      };
      CREATE LINK tail -> default::Node {
          ON TARGET DELETE ALLOW;
      };
      CREATE LINK priority -> default::Priority {
          ON TARGET DELETE ALLOW;
      };
      CREATE ANNOTATION std::description := 'Process..';
      CREATE LINK processType -> default::ProcessType {
          ON TARGET DELETE ALLOW;
      };
      CREATE LINK realiser -> default::User {
          ON TARGET DELETE ALLOW;
      };
      CREATE PROPERTY passport_ref -> std::str;
      CREATE REQUIRED PROPERTY title -> std::str {
          CREATE CONSTRAINT std::exclusive;
          CREATE CONSTRAINT std::max_len_value(50);
      };
  };
  CREATE TYPE default::Template EXTENDING default::Auditable {
      CREATE REQUIRED LINK process -> default::Process {
          ON TARGET DELETE ALLOW;
          CREATE CONSTRAINT std::exclusive;
      };
      CREATE ANNOTATION std::description := 'Template.';
      CREATE REQUIRED PROPERTY title -> std::str {
          CREATE CONSTRAINT std::max_len_value(50);
      };
  };
};
