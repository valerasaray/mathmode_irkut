module default {
    abstract type Auditable {
        annotation description := "Add 'create at property to all types.";
        required property created_at -> datetime {
            readonly := true;
            default := datetime_current();
        };
    }

    type Right extending Auditable {
        annotation description := "Right.";
        required property value -> str {
            constraint exclusive;
            constraint max_len_value(50);
        }
    }

    type User extending Auditable {
        annotation description := "User.";
        required property login -> str {
            constraint exclusive;
            constraint max_len_value(50);
        };
        property password -> str {
            constraint max_len_value(50);
        };
        property FIO -> str {
            constraint max_len_value(100);
        };
        multi link rights -> Right {
            on target delete allow;
        };
    }

    type Department extending Auditable {
        annotation description := "Department.";
        required property title -> str {
            constraint max_len_value(100);
        };
        link boss -> User {
            on target delete allow;
        };
        multi link staff -> User {
            on target delete allow;
        };
    }

    type Comment extending Auditable {
        annotation description := "Comment.";
        required property text_str -> str;
        link author -> User {
            on target delete allow;
        };
        property answer -> str;
    }

    type SubNode extending Auditable {
        annotation description := "SubNode.";
        required property title -> str {
            constraint max_len_value(50);
        };
        property start_verification -> datetime {
            default := datetime_current();
        };
        multi link comments -> Comment {
            on target delete allow;
        };
        link fit -> User {
            on target delete allow;
        };
        property end_verification -> datetime {
            default := datetime_current();
        };
        property end_correction -> datetime {
            default := datetime_current();
        };
        property main -> bool;
    }

    type TitleField extending Auditable {
        required property value -> str;
    }

    type Field extending Auditable {
        annotation description := "Field.";
        required property value -> str;
        link titleField -> TitleField {
            on target delete allow;
        };
    }

    type Status extending Auditable {
        annotation description := "Status.";
        required property title -> str {
            constraint exclusive;
        };
        required property color -> str {
            constraint exclusive;
        };
    }

    type Node extending Auditable {
        annotation description := "Node.";
        required property title -> str {
            constraint max_len_value(50);
        };
        multi link assigned -> Department {
            on target delete allow;
        };
        link along -> Node {
            on target delete allow;
        };
        property addenable -> bool;
        multi link subs -> SubNode {
            on target delete allow;
        };
        link next -> Node {
            on target delete allow;
        };
        multi link customField -> Field {
            on target delete allow;
        };
        link status -> Status {
            on target delete allow;
        };
        property receipt -> datetime;
    }
    
    type ProcessType extending Auditable {
        annotation description := "ProcessType.";
        required property title -> str {
            constraint max_len_value(50);
            constraint exclusive;
        };
    }    
    
    type Priority extending Auditable {
        annotation description := "Priority.";
        required property value -> str {
            constraint exclusive;
            constraint max_len_value(50);
        };
    }

    type Process extending Auditable {
        annotation description := "Process..";
        required property title -> str {
            constraint max_len_value(50);
        };
        link realiser -> User {
            on target delete allow;
        };
        link realiserGroup -> Department {
            on target delete allow;
        };
        link head -> Node {
            on target delete allow;
        };
        multi link nodes -> Node {
            on target delete allow;
        };
        link priority -> Priority {
            on target delete allow;
        };
        property passport_ref -> str;
        link processType -> ProcessType {
            on target delete allow;
        };
    }
    
    type Template extending Auditable {
        annotation description := "Template.";
        required property title -> str {
            constraint exclusive;
            constraint max_len_value(50);          
        };
        required link process -> Process {
            constraint exclusive;
            on target delete allow;
        };
    }

    type Notification extending Auditable {
        annotation description := "Notification.";
        link user_to -> User {
            on target delete allow;
        };
        link to_department -> Department {
            on target delete allow;
        };
        link comment -> Comment {
            on target delete allow;
        };
        link new_assign -> Process {
            on target delete allow;
        };
        multi link passed_node -> Node {
            on target delete allow;
        };
    }
}
