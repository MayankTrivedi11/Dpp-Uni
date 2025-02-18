// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CourseManagement {
    struct Course {
        uint id;
        string title;
        string description;
        string instructor;
    }

    Course[] public courses;
    uint public courseCount;

    event CourseAdded(uint id, string title, string instructor);

    function addCourse(string memory _title, string memory _description, string memory _instructor) public {
        courses.push(Course(courseCount, _title, _description, _instructor));
        emit CourseAdded(courseCount, _title, _instructor);
        courseCount++;
    }

    function getCourses() public view returns (Course[] memory) {
        return courses;
    }
}
