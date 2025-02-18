import React, { useEffect, useState } from 'react';
import axios from '../utils/api';

interface Course {
    _id: string;
    title: string;
    description: string;
    instructor: string;
}

const CourseList: React.FC = () => {
    const [courses, setCourses] = useState<Course[]>([]);

    useEffect(() => {
        axios.get('/courses')
            .then((response: { data: React.SetStateAction<Course[]>; }) => setCourses(response.data))
            .catch((error: any) => console.error("Error fetching courses:", error));
    }, []);

    return (
        <div>
            <h2>Courses</h2>
            <ul>
                {courses.map(course => (
                    <li key={course._id}>{course.title}</li>
                ))}
            </ul>
        </div>
    );
};

export default CourseList;
