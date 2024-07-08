import React from "react";

function Highlights({ stats }) {
  return (
    <div className="bg-slate-600 p-2 text-slate-200 flex flex-col justify-start items-center ">
      <h2 className="text-sm mt-2">{stats.title}</h2>
      <div className="mt-2">
        <span className="text-4xl font-bold">{stats.value}</span>
        <span className="text-2xl">{stats.unit}</span>
      </div>
      {/* {stats.direction? (
        <div className="flex mt-4">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            strokeWidth={1.5}
            stroke="currentColor"
            className="w-6 h-6 text-slate-200"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M6 12L3.269 3.126A59.768 59.768 0 0121.485 12 59.77 59.77 0 013.27 20.876L5.999 12zm0 0h7.5"
            />
          </svg>
          <div className="text-slate-200 ms-2">{stats.direction}</div>
        </div>
      ) : null} */}

      {stats.title == "Humidity"? (
        <div className="w-full mt-4 bg-gray-200 rounded-full h-1.5 mb-4 dark:bg-gray-700">
          <div
            className="bg-blue-600 h-1.5 rounded-full dark:bg-blue-500"
            style={{ width: `${stats.value}%` }}
          ></div>
        </div>
      ) : null}
    </div>
  );
}

export default Highlights;
