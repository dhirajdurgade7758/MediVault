// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PatientRecords {
    struct Record {
        string patientName;
        string diagnosis;
        string treatment;
        string ipfsHash; // For large records stored on IPFS
        uint timestamp;
    }

    mapping(uint => Record) public records;
    uint public recordCount;
    address public owner;

    event RecordStored(uint recordId, string patientName, string diagnosis, string treatment, string ipfsHash);

    constructor() {
        owner = msg.sender;
    }

    function storeRecord(string memory _patientName, string memory _diagnosis, string memory _treatment, string memory _ipfsHash) public {
        recordCount++;
        records[recordCount] = Record(_patientName, _diagnosis, _treatment, _ipfsHash, block.timestamp);
        emit RecordStored(recordCount, _patientName, _diagnosis, _treatment, _ipfsHash);
    }

    function getRecord(uint _recordId) public view returns (string memory, string memory, string memory, string memory, uint) {
        Record memory record = records[_recordId];
        return (record.patientName, record.diagnosis, record.treatment, record.ipfsHash, record.timestamp);
    }
}
