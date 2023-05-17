CREATE MIGRATION m1laxia3ese7qqi3bvg3xsytv7eonouubsnvq47aosnxswwuuwlxka
    ONTO m1ctvtssjhhil72q6ob5ojmfbflxqabc6t4kpi2kpui6hzkrxb3fca
{
  ALTER TYPE default::Process {
      DROP LINK tail;
      ALTER PROPERTY title {
          DROP CONSTRAINT std::exclusive;
      };
  };
};
