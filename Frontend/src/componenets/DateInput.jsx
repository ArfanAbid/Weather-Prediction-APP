import React, { useState } from "react";

const DateInput = ({ onDateChange }) => {
  const [date, setDate] = useState("");

  const handleDateChange = (event) => {
    setDate(event.target.value);
    onDateChange(event.target.value); // Notify parent component about the change
  };

  return (
    <>
      <div>
        <div>{/* location  */}</div>
        <div>
          <h1 className="text-slate-300  text-xl font-semibold p-1">
            Select date{" "}
          </h1>
          <input
            type="date"
            value={date}
            onChange={handleDateChange}
            className="border border-gray-300  bg-slate-500 text-slate-200 rounded-md p-2 w-full"
          />
          {/* <button onSubmit={handleDateChange} className="border border-gray-300 rounded-md p-2 w-full"> Submit </button> */}
        </div>
      </div>
    </>
  );
};

export default DateInput;
