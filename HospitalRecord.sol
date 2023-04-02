pragma solidity ^0.8.0;

contract HospitalRecord {
    struct User {
        address id;
        string name;
    }

    struct Prescription {
        uint256 id;
        string diagnosis;
    }

    // User Data
    mapping(address => User) public users;
    uint256 public userCount;

    // Prescription
    mapping(address => Prescription[]) public prescriptions;
    uint256 public prescriptionCount;

    function addUser(string memory name) public {
        address userId = msg.sender;
        users[userId].id = userId;
        users[userId].name = name;
        userCount++;
    }

    function addPrescription(address userId, string memory diagnosis) public {
        uint256 prescriptionId = prescriptionCount + 1;
        Prescription memory p = Prescription(prescriptionId, diagnosis);
        prescriptions[userId].push(p);
        prescriptionCount++;
    }

    function updatePrescription(
        address userId,
        uint256 prescriptionId,
        string memory diagnosis
    ) public {
        prescriptions[userId][prescriptionId].diagnosis = diagnosis;
    }
}
